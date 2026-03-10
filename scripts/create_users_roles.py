import boto3

# Connect to AWS IAM
iam = boto3.client('iam')

# Create groups
groups = ['Admins', 'Developers', 'Auditors']

for group in groups:
    try:
        iam.create_group(GroupName=group)
        print(f"Created group: {group}")
    except Exception as e:
            print(f"Group {group} may already exist: {e}")

# Create users and assign to groups
users = {
'admin_user': 'Admins',
'dev_user': 'Developers',
'auditor_user': 'Auditors'
}

for user, group in users.items():
    try:
        iam.create_user(UserName=user)
        iam.add_user_to_group(GroupName=group, UserName=user)
        print(f"Created user {user} in group {group}")
    except Exception as e:
            print(f"User {user} may already exist: {e}")

# Attach group policies
policies = {
'Admins': 'arn:aws:iam::aws:policy/AdministratorAccess',
'Developers': 'arn:aws:iam::aws:policy/PowerUserAccess',
'Auditors': 'arn:aws:iam::aws:policy/IAMReadOnlyAccess'
}

for group, policy_arn in policies.items():
    try:
        iam.attach_group_policy(GroupName=group, PolicyArn=policy_arn)
        print(f"Attached policy {policy_arn} to group {group}")
    except Exception as e:
            print(f"Error attaching policy to group {group}: {e}")
