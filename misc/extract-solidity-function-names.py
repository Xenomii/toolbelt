import solc
import json
from solc import install_solc, get_solc_version

# Install the latest version of the Solidity compiler
latest_version = get_solc_version().get('solc')
install_solc(latest_version)

# Compile the Solidity contract
with open('contract.sol', 'r') as f:
    contract_source_code = f.read()

compiled_sol = solc.compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:MyContract']

# Get the ABI of the contract
abi = contract_interface['abi']

# Extract the function names from the ABI
function_names = []
for item in abi:
    if item['type'] == 'function':
        function_names.append(item['name'])

# Print the function names
print("Function names:")
for name in function_names:
    print(name)

