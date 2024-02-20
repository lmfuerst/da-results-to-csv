import os
import json
import csv

# EThor: xyz insecure
# Mythril: {"error": null, "issues": [{"address": 705, "contract": "MAIN", "description": "Read of persistent state following external call\nThe contract account state is accessed after an external call to a fixed address. To prevent reentrancy issues, consider accessing the state only before the call, especially if the callee is untrusted. Alternatively, a reentrancy lock can be used to prevent untrusted callees from re-entering the contract in an intermediate state.", "function": "withdraw(uint256)", "max_gas_used": 64108, "min_gas_used": 8832, "severity": "Low", "sourceMap": 705, "swc-id": "107", "title": "State access after external call", "tx_sequence": {"initialState": {"accounts": {"0x0": {"balance": "0x0", "code": "60806040526004361061006c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168062362a951461007157806327e235e3146100a75780632e1a7d4d146100fe578063db0fb1071461012b578063f8b2cb4f1461016e575b600080fd5b6100a5600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506101c5565b005b3480156100b357600080fd5b506100e8600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610214565b6040518082815260200191505060405180910390f35b34801561010a57600080fd5b506101296004803603810190808035906020019092919050505061022c565b005b34801561013757600080fd5b5061016c600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506102cd565b005b34801561017a57600080fd5b506101af600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610368565b6040518082815260200191505060405180910390f35b346000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555050565b60006020528060005260406000206000915090505481565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020541015156102ca5761027d33826103b0565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055505b50565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614156103655780600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b50565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b600063d0679d347c0100000000000000000000000000000000000000000000000000000000029050600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16817c0100000000000000000000000000000000000000000000000000000000900484846040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050600060405180830381865af492505050505050505600a165627a7a723058206b3a29b45d50ef55b397e8979614acb71d8f99c267f5179bb3a9490b374f3a4d0029", "nonce": 0, "storage": "{}"}, "0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef": {"balance": "0x0", "code": "", "nonce": 0, "storage": "{}"}}}, "steps": [{"address": "0x0", "calldata": "0x2e1a7d4d", "input": "0x2e1a7d4d", "name": "withdraw(uint256)", "origin": "0xaffeaffeaffeaffeaffeaffeaffeaffeaffeaffe", "resolved_input": null, "value": "0x0"}]}}, {"address": 712, "contract": "MAIN", "description": "Write to persistent state following external call\nThe contract account state is accessed after an external call to a fixed address. To prevent reentrancy issues, consider accessing the state only before the call, especially if the callee is untrusted. Alternatively, a reentrancy lock can be used to prevent untrusted callees from re-entering the contract in an intermediate state.", "function": "withdraw(uint256)", "max_gas_used": 64108, "min_gas_used": 8832, "severity": "Low", "sourceMap": 712, "swc-id": "107", "title": "State access after external call", "tx_sequence": {"initialState": {"accounts": {"0x0": {"balance": "0x0", "code": "60806040526004361061006c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168062362a951461007157806327e235e3146100a75780632e1a7d4d146100fe578063db0fb1071461012b578063f8b2cb4f1461016e575b600080fd5b6100a5600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506101c5565b005b3480156100b357600080fd5b506100e8600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610214565b6040518082815260200191505060405180910390f35b34801561010a57600080fd5b506101296004803603810190808035906020019092919050505061022c565b005b34801561013757600080fd5b5061016c600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506102cd565b005b34801561017a57600080fd5b506101af600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610368565b6040518082815260200191505060405180910390f35b346000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555050565b60006020528060005260406000206000915090505481565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020541015156102ca5761027d33826103b0565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055505b50565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614156103655780600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b50565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b600063d0679d347c0100000000000000000000000000000000000000000000000000000000029050600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16817c0100000000000000000000000000000000000000000000000000000000900484846040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050600060405180830381865af492505050505050505600a165627a7a723058206b3a29b45d50ef55b397e8979614acb71d8f99c267f5179bb3a9490b374f3a4d0029", "nonce": 0, "storage": "{}"}, "0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef": {"balance": "0x0", "code": "", "nonce": 0, "storage": "{}"}}}, "steps": [{"address": "0x0", "calldata": "0x2e1a7d4d", "input": "0x2e1a7d4d", "name": "withdraw(uint256)", "origin": "0xaffeaffeaffeaffeaffeaffeaffeaffeaffeaffe", "resolved_input": null, "value": "0x0"}]}}, {"address": 1195, "contract": "MAIN", "description": "The return value of a message call is not checked.\nExternal calls return a boolean value. If the callee halts with an exception, 'false' is returned and execution continues in the caller. The caller should check whether an exception happened and react accordingly to avoid unexpected behavior. For example it is often desirable to wrap external calls in require() so the transaction is reverted if the call fails.", "function": "withdraw(uint256)", "max_gas_used": 64108, "min_gas_used": 8832, "severity": "Medium", "sourceMap": 1195, "swc-id": "104", "title": "Unchecked return value from external call.", "tx_sequence": {"initialState": {"accounts": {"0x0": {"balance": "0x0", "code": "60806040526004361061006c576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168062362a951461007157806327e235e3146100a75780632e1a7d4d146100fe578063db0fb1071461012b578063f8b2cb4f1461016e575b600080fd5b6100a5600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506101c5565b005b3480156100b357600080fd5b506100e8600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610214565b6040518082815260200191505060405180910390f35b34801561010a57600080fd5b506101296004803603810190808035906020019092919050505061022c565b005b34801561013757600080fd5b5061016c600480360381019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506102cd565b005b34801561017a57600080fd5b506101af600480360381019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610368565b6040518082815260200191505060405180910390f35b346000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555050565b60006020528060005260406000206000915090505481565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020541015156102ca5761027d33826103b0565b806000803373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055505b50565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614156103655780600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505b50565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020549050919050565b600063d0679d347c0100000000000000000000000000000000000000000000000000000000029050600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16817c0100000000000000000000000000000000000000000000000000000000900484846040518363ffffffff167c0100000000000000000000000000000000000000000000000000000000028152600401808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200192505050600060405180830381865af492505050505050505600a165627a7a723058206b3a29b45d50ef55b397e8979614acb71d8f99c267f5179bb3a9490b374f3a4d0029", "nonce": 0, "storage": "{}"}, "0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef": {"balance": "0x0", "code": "", "nonce": 0, "storage": "{}"}}}, "steps": [{"address": "0x0", "calldata": "0x2e1a7d4d", "input": "0x2e1a7d4d", "name": "withdraw(uint256)", "origin": "0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef", "resolved_input": null, "value": "0x0"}, {"address": "0x0", "calldata": "0x2e1a7d4d", "input": "0x2e1a7d4d", "name": "withdraw(uint256)", "origin": "0xdeadbeefdeadbeefdeadbeefdeadbeefdeadbeef", "resolved_input": null, "value": "0x0"}]}}], "success": true}
# Sailfish: DAO dependency detected


rootdir = "./results_delegate"

if __name__ == "__main__":
    dictionary_list = []

    for subdir, dirs, files in os.walk(rootdir):
        if any(file.endswith(".json") for file in os.listdir(subdir)):
            dictionary = {}
            print(subdir)
            split = subdir.split("\\")
            dictionary["tool"] = split[1]
            dictionary["name"] = split[3]
            dictionary["error"] = ""

            if any(file.endswith(".log") for file in os.listdir(subdir)):
                with open(os.path.join(subdir, "result.log")) as f:
                    insecure = False
                    for line in f.readlines():
                        if ".hex insecure" in line \
                                or '"swc-id": "107"' in line \
                                or "DAO dependency detected" in line \
                                or "Re-Entrancy Vulnerability: 		 True" in line:
                            insecure = True
                        if "Traceback (most recent call last)" in line \
                                or "Exception in thread" in line \
                                or "ERROR:" in line:
                            dictionary["error"] = True
                        if '"error": null' not in line and '"error":' in line:
                            dictionary["error"] = True

                    dictionary["reentrant"] = insecure

            else:
                dictionary["reentrant"] = ""

            with open(os.path.join(subdir, "smartbugs.json")) as f:
                data = json.load(f)
                fullname = data["filename"]
                dictionary["filename"] = fullname
                if "testdata" in fullname:
                    split2 = fullname.split("\\")
                    print(fullname)
                    dictionary["sol_version"] = split2[10]
                    dictionary["type"] = split2[9]
                    if "\\No\\" in fullname:
                        dictionary["ground_truth"] = False
                    elif "\\Reentrant\\" in fullname:
                        dictionary["ground_truth"] = True
                    else:
                        dictionary["ground_truth"] = ""

            if "testdata" in dictionary["filename"]:
                dictionary_list.append(dictionary)

    # write to csv
    with open("results_csv_gt_delegate.csv", 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';',
                                fieldnames=["tool", "sol_version", "type", "name", "reentrant", "error",
                                            "ground_truth", "filename"])
        writer.writeheader()
        for data in dictionary_list:
            writer.writerow(data)
