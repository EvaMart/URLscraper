<-- http://pydoit.org-->

doit - go to homepage __ __ Toggle navigation__
# **doit** comes from the idea of bringing the power of **build-tools** to execute any kind of **task**
People often compare **doit** to tools like _make_, _grunt_, _rake_, _scons_, _snakemake_.
They appreciate **doit** strong features, flexibility, simplicity of authoring and ease of use.
## A **game developer** uses `doit` to
* Automate all project related tasks (code generation, cross-compilation, resource generation)
* Simplify cumbersome command line calls
* Optimize processing time by skipping tasks already done
## A **bioinformatics developer** uses `doit` to
* Create a reproduceable computational pipeline
* Manage a complex workflow (set of depending tasks)
* Optimize processing time by skipping tasks already done
## Nikola, a **static site generator**, uses `doit` to
* Provide the command line interface
* Speed up by parallel task execution
* Optimize processing time by skipping tasks already done
Define functions returning python _dict_ with task's meta-data.
"""find imports from a python module"""
for name, module in PKG_MODULES.by_name.items():
'actions': [(get_imports, (PKG_MODULES, module.path))],
"""generate a graphviz's dot graph from module imports"""
'getargs': {'imports': ('imports', 'modules')},
"""generate image from a dot file"""
'actions': ['dot -Tpng %(dependencies)s -o %(targets)s'],
dot       generate a graphviz's dot graph from module imports
draw      generate image from a dot file
imports   find imports from a python module
_doit_ allows you to easily define ad-hoc tasks, helping you to organize all your project related tasks in an unified easy-to-use & discoverable way.
_doit_ uses plain python to define tasks.
Task's meta-data are better described in a declarative way, but often you want to create this meta-data programmatically.
_NO API_: Tasks are described by a python _dict_ (can also be easily customized)
Tasks can execute external process (shell commands) or python code
### debugger & self documented
Since plain python is used to define your tasks the python debugger _pdb_ is available
_doit_ command allows you to list and obtain help/documentation for tasks
## Build tool & Pipelines
Simple task runners simply do not scale-up. _doit_ as other build-tools can be much more efficient at repeateadly running tasks.
### cache task results 
_doit_ creates a DAG and ensures that only required tasks will be executed and in the correct order.
_doit_ checks if the task is _up-to-date_ and skips its execution if the task would produce the same result of a previous execution.
_dependencies_ can be dynamically calculated by other tasks
the _up-to-date_ check to cache task results is not restricted to looking for file modification on dependencies. Nor requires _target_ files.
Traditional build-tools were created mainly to deal with compile/link process of source code. _doit_ was designed to solve a broader range of workflows.
results from a task can be used by another task without resorting to the creation of intermediate files
Command line output can be completely customized through _reporters_
allow you to create/modify sub-commands, storage backend, task loader, and output reporter
API is exposed so you can create new applications/tools leveraging _doit_ functionality
built-in support for parallel (threaded or multi-process) task execution
built-in support watching for file changes and automatically re-execute tasks based on file changes by external process [linux/mac only]
built-in support tab-completion for commands/task (supports _bash_ and _zsh_)
create task's dependency-graph image using _graphviz_
IPython integration provide `%doit` magic function that loads tasks defined directly in IPython's global namespace
Integration with _strace_ helps you understand effects of third-part commands
* Congratulations! **Your tool follows the KISS principle very closely**. I always wondered why build tools had to be that complicated.
* Let me start by saying I'm really lovin doit, at first the interface seemed verbose but quickly changed my mind when **I started using it and realized the flexibility**. Many thanks for the great software!
* I love all the traditional unix power tools, like cron, `make`, perl, ..., I also like new comprehensive configuration management tools like `CFEngine` and `Puppet`. But **I find doit to be so versatile and so productive**.
* I needed a sort of `make` tool to glue things together and after trying out all kinds, **doit ... has actually turned out to be beautiful**. Its easy to add and manage tasks, even complex ones-- gluing things together with decorators and 'library' functions I've written to do certain similar things.
* I went back and forth on different Pythonic build tools for awhile. `Scons` is pretty great if you're doing 'standard' sorts of builds, but I found it a little heavy for my tastes and really hard to customize to my tool flow (in `FPGA` land, there are all kinds of nonstandard vendor tools that all need to play together). I've been using doit more and more over the past few months, and I'm continually impressed by the tool (aside from the goofy name). **It works amazingly well for automating tricky/exotic build processes**. Check it out!
* Some time ago, I grew frustrated with `Make` and `Ant` and started porting my build files to every build tool I found (`SCons`, `Waf`, etc.). Each time, as soon as I stepped out of already available rules, I ran into some difficult to overcome stumbling blocks. **Then I discovered this little gem of simplicity: doit**. It's Python-based. It doesn't try to be smart, it does not try to be cool, it just works. If you are looking for a flexible little build tool for different languages and tasks, give it a chance. (...)
`doit` is under active development. Version 0.31 released on 2018-02.
_doit_ runs on Python 3.4 through 3.6 (including PyPy). For python 2 support please use _doit_ version `0.29`.
This blog post explains how everything started in 2008.
_doit_ core features are quite stable. If there is no recent development, it does NOT mean the project is not being maintained... The project has 100% unit-test code coverage.
Development is done based on real world use cases. It is well designed and has a small code base, so adding new features is not hard. Contributions are welcome.
This is an open-source project (MIT license) written in python. 
Project management (bug tracker, feature requests and source code ) on github
This web site is hosted on http://pages.github.com 
Powered by Universal template and Sphinx.
© 2018. pydoit.org / Eduardo Schettino (schettino72)
Template design by Bootstrapious Templates