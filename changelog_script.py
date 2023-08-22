import sys
import requests

GITHUB_TOKEN = '<TOKEN>'
ORG_NAME = 'your-organization'
REPO_NAME = 'your-repo'

def get_pull_request(pull_request_number):
    url = f'https://api.github.com/repos/{ORG_NAME}/{REPO_NAME}/pulls/{pull_request_number}'
    headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    response = requests.get(url, headers=headers)
    return response.json()

def manual_input(prompt):
    user_input = input(prompt)
    return user_input.strip()

def generate_changelog_entry(pull_request):
    changelog_entry = ""

        # Automatic Parameter Population
    # if 'Added' in pull_request['labels']:
        # changelog_entry += f"### Added\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n"
        # # Add logic to process pull request body, if needed.

    # if 'Changed' in pull_request['labels']:
        # changelog_entry += f"### Changed\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n"
        # # Add logic to process pull request body, if needed.

    # if 'Fixed' in pull_request['labels']:
        # changelog_entry += f"### Fixed\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n"
        # # Add logic to process pull request body, if needed.

    # if 'Removed' in pull_request['labels']:
        # changelog_entry += f"### Removed\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n"
        # # Add logic to process pull request body, if needed.
        
        
        # Manual Parameter Population
    if 'Added' in pull_request['labels']:
        user_input = manual_input("Enter added details: ")
        changelog_entry += f"### Added\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n  Details: {user_input}\n"

    if 'Changed' in pull_request['labels']:
        user_input = manual_input("Enter changed details: ")
        changelog_entry += f"### Changed\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n  Details: {user_input}\n"

    if 'Fixed' in pull_request['labels']:
        user_input = manual_input("Enter fixed details: ")
        changelog_entry += f"### Fixed\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n  Details: {user_input}\n"

    if 'Removed' in pull_request['labels']:
        user_input = manual_input("Enter removed details: ")
        changelog_entry += f"### Removed\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n  Details: {user_input}\n"

    if 'Documentation' in pull_request['labels']:
        user_input = manual_input("Enter documentation details: ")
        changelog_entry += f"### Documentation\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n  Details: {user_input}\n"

    if 'Miscellaneous' in pull_request['labels']:
        user_input = manual_input("Enter miscellaneous details: ")
        changelog_entry += f"### Miscellaneous\n- {pull_request['title']} (#{pull_request['number']}) - {pull_request['user']['login']}\n  Details: {user_input}\n"

    return changelog_entry

def update_changelog_file(changelog_entry):
    # Implement updating the CHANGELOG.md file
    # Open the file, append the changelog_entry, and save the changes
    with open('CHANGELOG.md', 'a') as changelog_file:
        changelog_file.write(changelog_entry)

def main(pull_request_number):
    pull_request = get_pull_request(pull_request_number)
    changelog_entry = generate_changelog_entry(pull_request)
    update_changelog_file(changelog_entry)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python changelog_script.py <pull_request_number>")
        sys.exit(1)

    pull_request_number = sys.argv[1]
    main(pull_request_number)