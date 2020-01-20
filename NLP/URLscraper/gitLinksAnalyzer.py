from checkGit import isNameInRepoName


def cutLinkToShortest(link, tool_name):
    fields = link.split("/")

    for a in range(len(fields)):
        new_link = "/".join(fields[:-a])
        if isNameInRepoName(tool_name, new_link):
            shortest_link = new_link
        else:
            continue

    print("Shortest url containing name: %s" % (shortest_link))
    labels = ["github", "sourceforge", "gitlab"]
    if True not in [a in shortest_link for a in labels]:
        print("But it is not a valid repository link")

    else:
        print("This is a valid repository link")
    return shortest_link


if __name__ == "__main__":

    with open(
        "/home/eva/mining/scraper/URLscraper/500urlsOut_githubFindings.txt", "r"
    ) as gitOutFile:
        tools_dict = {}  #############we are here

        """
        tools_dict = {
            "tool_name": {
                "matching_githubs" : [],
                "non_matching_githubs" : []
            },
            ...
        }

        """

        lines = gitOutFile.readlines()[1:]  # first row is header

        with open("github_non_matching.txt", "w") as non_matching_out:

            with open("github_matching.txt", "w") as matching_out:

                for line in lines:
                    columns = line.split("\t")
                    columns[-1] = columns[-1].strip()

                    original_url = columns[0]
                    tool_name = columns[1]
                    github = columns[2]
                    score = columns[3]

                    if tool_name not in tools_dict.keys():

                        # "initialization of item in tool_dict dictionary"

                        tools_dict[tool_name] = {
                            "matching_githubs": [],
                            "non_matching_githubs": [],
                        }

                    if int(score) == 1:  # if matching

                        tools_dict[tool_name]["matching_githubs"].append(github)
                        matching_out.write(line)

                    else:

                        tools_dict[tool_name]["non_matching_githubs"].append(github)
                        non_matching_out.write(line)

        """
        # Getting a repo from the matching links
        # Keep the longest common substring that contains the name of the tool
        """

        print(
            "Total number or analyzed URLs was: 357 (urls used as input had 499 URLs)"
        )
        print("Tools for which a repository was found: %d" % len(tools_dict))
        print(
            "ratio of URLs containing any kind of github links: %.2f"
            % (len(tools_dict) / 357)
        )
        print("\n")
        matching_tools = [
            tools_dict[tool]
            for tool in tools_dict.keys()
            if len(tools_dict[tool]["matching_githubs"]) > 0
        ]
        print(
            "Tools for which a matching repository was found: %d" % len(matching_tools)
        )
        print(
            "Ratio of URLs containing any a matching repository name link: %.2f"
            % (len(matching_tools) / 357)
        )

        """
    # If this does not exist, keep the shortest strings that contain the name (splitting by /)
    from difflib import SequenceMatcher # standard lib
    match = SequenceMatcher(None, string1, string2).find_longest_match(0, len(string1), 0, len(string2))

    print(match)  # -> Match(a=0, b=15, size=9)
    print(string1[match.a: match.a + match.size])  # -> apple pie
    print(string2[match.b: match.b + match.size])  # -> apple pie
    """
