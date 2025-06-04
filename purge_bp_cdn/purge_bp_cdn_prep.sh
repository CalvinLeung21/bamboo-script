if ! python -c "import byteplus_sdk" &>/dev/null; then
  [[ $(id -u) -eq 0 ]] && sudo_opts= || sudo_opts="--user"
  python -m pip install $sudo_opts --upgrade wheel byteplus-sdk
fi
