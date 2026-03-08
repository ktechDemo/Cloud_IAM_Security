import boto3

# Create an IAM client
iam = boto3.client('iam')

# List of users to check MFA status
users = ['admin_user', 'dev_user', 'auditor_user']

# Check MFA for each user
for user in users:
    print(f"Checking MFA for {user}...")  # Debugging line
    mfa_devices = iam.list_mfa_devices(UserName=user)['MFADevices']

    if not mfa_devices:
        print(f"[ALERT] {user} does NOT have MFA enabled!")
    else:
        print(f"{user} has MFA enabled.")