NFT_SALES_TEMPLATE = {
  "type": "nft-sales",
  "templateId": "",
  "name": "nftSalesAgreement",
  "description": "This service agreement defines the flow for selling a NFT between users",
  "creator": "",
  "serviceAgreementTemplate": {
    "contractName": "NFTSalesTemplate",
    "events": [
      {
        "name": "AgreementCreated",
        "actorType": "consumer",
        "handler": {
          "moduleName": "nftSalesTemplate",
          "functionName": "fulfillLockPaymentCondition",
          "version": "0.1"
        }
      }
    ],
    "fulfillmentOrder": [
      "lockPayment.fulfill",
      "transferNFT.fulfill",
      "escrowPayment.fulfill"
    ],
    "conditionDependency": {
      "lockPayment": [],
      "transferNFT": [],
      "escrowPayment": [
        "lockPayment",
        "transferNFT"
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
              "functionName": "fulfillTransferNFTCondition",
              "version": "0.1"
            }
          }
        ]
      },
      {
        "name": "transferNFT",
        "timelock": 0,
        "timeout": 0,
        "contractName": "TransferNFTCondition",
        "functionName": "fulfill",
        "parameters": [
          {
            "name": "_documentId",
            "type": "bytes32",
            "value": ""
          },
          {
            "name": "_receiver",
            "type": "address",
            "value": ""
          },
          {
            "name": "_numberNfts",
            "type": "uint256",
            "value": ""
          },
          {
            "name": "_nftHolder",
            "type": "address",
            "value": ""
          },
          {
            "name": "_conditionId",
            "type": "bytes32",
            "value": ""
          }
        ],
        "events": [
          {
            "name": "Fulfilled",
            "actorType": "publisher",
            "handler": {
              "moduleName": "transferNFT",
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
        "contractName": "EscrowPayment",
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