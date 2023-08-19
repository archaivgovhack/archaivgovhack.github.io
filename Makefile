##
# Language of Leadership
#
# @Natural Language Processing Data Science Project
# @Author: Thaum (https://thaum.io)

SHELL=/bin/bash
#: #-> GENERAL
help: #-> displays this help
	@echo "Language of Leadership - Data Science Project - Thaum - https://thaum.io"
	@echo "========================================================================"
	@cat Makefile | grep -v "cat Makefile" | grep -E "^(.+):\s+#->"  | sed -E 's|^#:\s#->\s(.+)|\n\1|g' | sed -E 's|^#:(.+)|  \1|g'

#: #-> SYSTEM SETUP
reqs/submodules: #-> pulls / updates git submodules
	git submodule update --recursive --remote --init


# end
