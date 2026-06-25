list:
    just --list

run arg1="" arg2="" arg3="":
    uv run src/<app_name>/main.py {{arg1}} {{arg2}} {{arg3}}

test arg1="":
    uv run -m pytest {{arg1}}
