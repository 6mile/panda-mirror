import sys
import subprocess
import json
import requests
from datetime import datetime



# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)

print()
print("This script tests to see what version of a npm package different registries have.")
print("Test run at:", dt)
print()


def get_package_info(registry_url, package_name):
    try:
        # Configure npm to use specific registry
        subprocess.run(['npm', 'config', 'set', 'registry', registry_url], 
                      capture_output=True, text=True)
        
        # Run npm view with JSON output
        result = subprocess.run(['npm', 'view', package_name, '--json'], 
                              capture_output=True, text=True)
        
        # Parse the JSON output
        package_info = json.loads(result.stdout)
        
        # Get the tarball URL if available
        if 'dist' in package_info and 'tarball' in package_info['dist']:
            return {
                'registry': registry_url,
                'tarball': package_info['dist']['tarball'],
                'version': package_info.get('version', 'unknown')
            }
    except Exception as e:
        return {
            'registry': registry_url,
            'error': str(e)
        }
    
    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <package-name>")
        sys.exit(1)

    package_name = sys.argv[1]
    registries = [
        "https://registry.npmjs.org/",
        "https://r.cnpmjs.org/",
        "https://registry.npmmirror.com/",
        "https://repos.refinery.dev/repository/npm/",
        "https://repo.huaweicloud.com/repository/npm/",
        "https://mirrors.cloud.tencent.com/npm/",
        "https://registry.npm.taobao.org/",
	"https://npm-mirror.gitverse.ru/"
    ]

    print(f"Checking package '{package_name}' across {len(registries)} registries...\n")
    
    for registry in registries:
        print(f"Registry: {registry}")
        result = get_package_info(registry, package_name)
        
        if result:
            if 'error' in result:
                print(f"Error: {result['error']}")
            else:
                print(f"Version: {result['version']}")
                print(f"Tarball: {result['tarball']}")
        else:
            print("No package information found")
        print("-" * 80 + "\n")

if __name__ == "__main__":
    main()
