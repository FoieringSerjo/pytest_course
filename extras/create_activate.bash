# stick this in .bashrc or .zshrc
# create, activate, exit

function create {
  if [[ $# -gt 0 ]]
  then
    echo "python3 -m venv venv --prompt $1"
    python3 -m venv venv --prompt $1
  else 
    echo "python3 -m venv venv --prompt ."
    python3 -m venv venv --prompt .
  fi

  echo "venv/bin/python3 -m pip install -U pip"
  venv/bin/python3 -m pip install -U pip

  echo "source venv/bin/activate"
  source venv/bin/activate

}


function activate {
  if [ -d venv ]
  then
    echo "source venv/bin/activate"
    source venv/bin/activate
  fi
}

function exit {
    if [[ $(which python3) == *"venv"* ]]
    then
      echo "deactivate"
      deactivate
    else
      echo "no venv activated"
    fi
}
