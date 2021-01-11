if command - v pyenv 1>dev/null 2>&1; then
  eval "$(pyenv init -)"
fi
export "$(pyenv init -)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"