ACCESS_SLA_TEMPLATE = {
  "type": "Access",
  "templateId": "",
  "name": "dataAssetAccessServiceAgreement",
  "description": "This service agreement defines the flow for accessing a data asset on the network. Any file or bundle of files can be access using this service agreement",
  "creator": "",
  "serviceAgreementTemplate": {
    "contractName": "AccessTemplate",
    "events": [
      {
        "name": "AgreementCreated",
        "actorType": "consumer",
        "handler": {
          "moduleName": "escrowAccessTemplate",
          "functionName": "fulfillLockPaymentCondition",
          "version": "0.1"
        }
      }
    ],
    "fulfillmentOrder": [
      "lockPayment.fulfill",
      "access.fulfill",
      "escrowPayment.fulfill"
    ],
    "conditionDependency": {
      "lockPayment": [],
      "access": [],
      "escrowPayment": [
        "lockPayment",
        "access"
      ]
    },
    "conditions": [
      {
        "name": "lockPayment",
        "timelock": 0,
        "timeout": 0,
        "contractName": "LockPaymentCondition",
        "functionName": "fulfill",
        "parameters": [
          {
            "name": "_did",
            "type": "bytes32",
            "value": ""
          },
          {
            "name": "_rewardAddress",
            "type": "address",
            "value": ""
          },
          {
            "name": "_tokenAddress",
            "type": "address",
            "value": ""
          },
          {
            "name": "_amounts",
            "type": "uint256[]",
            "value": []
          },
          {
            "name": "_receivers",
            "type": "address[]",
            "value": []
          }
        ],
        "events": [
          {
            "name": "Fulfilled",
            "actorType": "publisher",
            "handler": {
              "moduleName": "lockPaymentCondition",
              "functionName": "fulfillAccessCondition",
              "version": "0.1"
            }
          }
        ]
      },
      {
        "name": "access",
        "timelock": 0,
        "timeout": 0,
        "contractName": "AccessCondition",
        "functionName": "fulfill",
        "parameters": [
          {
            "name": "_documentId",
            "type": "bytes32",
            "value": ""
          },
          {
            "name": "_grantee",
            "type": "address",
            "value": ""
          }
        ],
        "events": [
          {
            "name": "Fulfilled",
            "actorType": "publisher",
            "handler": {
              "moduleName": "access",
              "functionName": "fulfillEscrowPaymentCondition",
              "version": "0.1"
            }
          },
          {
            "name": "TimedOut",
            "actorType": "consumer",
            "handler": {
              "moduleName": "access",
              "functionName": "fulfillEscrowPaymentCondition",
              "version": "0.1"
            }
          }
        ]
      },
      {
        "name": "escrowPayment",
        "timelock": 0,
        "timeout": 0,
        "contractName": "EscrowPaymentCondition",
        "functionName": "fulfill",
        "parameters": [
          {
            "name": "_did",
            "type": "bytes32",
            "value": ""
          },
          {
            "name": "_amounts",
            "type": "uint256[]",
            "value": []
          },
          {
            "name": "_receivers",
            "type": "address[]",
            "value": []
          },
          {
            "name": "_sender",
            "type": "address",
            "value": ""
          },
          {
            "name": "_tokenAddress",
            "type": "address",
            "value": ""
          },
          {
            "name": "_lockCondition",
            "type": "bytes32",
            "value": ""
          },
          {
            "name": "_releaseCondition",
            "type": "bytes32",
            "value": ""
          }
        ],
        "events": [
          {
            "name": "Fulfilled",
            "actorType": "publisher",
            "handler": {
              "moduleName": "escrowPaymentCondition",
              "functionName": "verifyRewardTokens",
              "version": "0.1"
            }
          }
        ]
      }
    ]
  }
}
