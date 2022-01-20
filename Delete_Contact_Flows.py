import boto3
import json
from pprint import pprint
import datetime

azn_connect = boto3.client("connect")
instances_raw = azn_connect.list_instances()
# creates a variables that just contains the Instance list
instances = instances_raw["InstanceSummaryList"]
instances_num = len(instances)


print("-" * 50)
print("-" * 50)
print("\nNumber of Instances : " + str(instances_num))
print("-" * 50)
print("-" * 50)


for instance in instances:
    instance_Id = instance["Id"]
    print("*" * 50)
    print("*" * 50)
    print("Connect Instance Alias : " + instance["InstanceAlias"])
    print("Connect Instance ARN : " + instance["Arn"])
    print("Connect Instance ID : " + instance["Id"])
    print("*" * 50)
    print("*" * 50)

    contact_flows_raw = azn_connect.list_contact_flows(InstanceId=instance_Id)
    contact_flows = contact_flows_raw["ContactFlowSummaryList"]
    contact_flow_num = len(contact_flows)

    print("\nNumber of Contact Flows : " + str(contact_flow_num))
    print("+" * 40)
    print()
    print("------Default Contact Flows------")
    print("+" * 40)
    for contact_flow in contact_flows:
        if ("Default" in contact_flow["Name"]) or (
            "Sample" in contact_flow["Name"]
        ):
            print(contact_flow["Name"])
            print(contact_flow["Id"])
            print(contact_flow["Arn"])
            print("-" * 100)
    print("-----Student Contact Flows-------")
    print("+" * 40)
    for contact_flow in contact_flows:
        if ("Default" not in contact_flow["Name"]) and (
            "Sample" not in contact_flow["Name"]
        ):
            print(contact_flow["Name"])
            print(contact_flow["Id"])
            print(contact_flow["Arn"])
            print("-" * 100)
            print("DELETING the Student Contact Flows")
            delete_contact_flow = azn_connect.delete_contact_flow(
                InstanceId=instance_Id, ContactFlowId=contact_flow["Id"]
            )
            print(delete_contact_flow["ResponseMetadata"]["HTTPStatusCode"])
            print("-----------")
