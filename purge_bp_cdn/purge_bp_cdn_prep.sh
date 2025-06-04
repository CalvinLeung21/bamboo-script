# Ensure pip is installed
if ! python3 -m pip -V &>/dev/null; then
  python3 -m ensurepip --upgrade || {
    echo "pip is not available and cannot be bootstrapped. Please install it manually."
    exit 1
  }
fi

# Install byteplus_sdk if not available
if ! python3 -c "import byteplus_sdk" &>/dev/null; then
  opts=$( [ "$(id -u)" -eq 0 ] && echo "" || echo "--user" )
  python3 -m pip install $opts --upgrade wheel byteplus-sdk
fi
