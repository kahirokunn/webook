if [ $# != 1 ]; then
  echo 引数には1つのパスを指定してください
else
  script="pycodestyle --config pycodestyle.config $1"
  eval ${script}
  script="flake8 --inline-quotes \"'\" $1 | grep \"Remove bad quotes.\""
  eval ${script}
  script="grep -r \"def __\" $1 | grep -v \"def\ __\w\+__\""
  eval ${script}
fi

