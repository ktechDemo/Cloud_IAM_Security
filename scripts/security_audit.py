import boto3
import json

# Create an IAM client
iam = boto3.client('iam')

# List all IAM users
users = iam.list_users()['Users']

# Prepare the audit report
audit_report = []

# Loop through each user and check their MFA status and attached policies
for user in users:
    user_name = user['UserName']
    print(f"Checking MFA and policies for {user_name}...")  # Debugging line

    # Check if MFA is enabled for this user
    mfa_devices = iam.list_mfa_devices(UserName=user_name)['MFADevices']
    has_mfa = bool(mfa_devices)

    # List policies attached to the user
    attached_policies = iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
    policies = [policy['PolicyName'] for policy in attached_policies]

    # Add user data to audit report
    audit_report.append({
        'UserName': user_name,
        'HasMFA': has_mfa,
        'Policies': policies
    })

    # Print out the audit details for each user (optional debug line)
    print(f"User: {user_name}, MFA: {'Enabled' if has_mfa else 'Not Enabled'}, Policies: {', '.join(policies)}")

# Save the audit report to a JSON file
with open('audit_report.json', 'w') as f:
    json.dump(audit_report, f, indent=4)

print("Security audit complete. Report saved as audit_report.json")
