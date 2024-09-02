import sys
print("Python executable used:", sys.executable)
import os
import yaml
import requests

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def convert_yaml(input_yaml, start_port):
    try:
        yaml_data = yaml.safe_load(input_yaml)
        
        num_proxies = len(yaml_data['proxies'])
        
        new_yaml = {
            'allow-lan': True,
            'dns': {
                'enable': True,
                'enhanced-mode': 'fake-ip',
                'fake-ip-range': '198.18.0.1/16',
                'default-nameserver': ['114.114.114.114'],
                'nameserver': ['https://doh.pub/dns-query']
            },
            'listeners': [],
            'proxies': yaml_data['proxies']
        }
        
        new_yaml['listeners'] = [
            {
                'name': f'mixed{i}',
                'type': 'mixed',
                'port': start_port + i,
                'proxy': yaml_data['proxies'][i]['name']
            } for i in range(num_proxies)
        ]
        
        return yaml.dump(new_yaml, allow_unicode=True)
    
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    input_url = os.environ.get('CONFIG_URL')
    start_port = int(os.environ.get('START_PORT', 40000))
    output_file = "/root/.config/mihomo/config.yaml"
    
    if not input_url:
        print("Error: CONFIG_URL environment variable is not set.")
        exit(1)
    
    # Fetch YAML data from the provided URL
    input_yaml = fetch_data(input_url)
    
    # Convert the YAML data
    output_yaml = convert_yaml(input_yaml, start_port)
    
    if output_yaml:
        # Save the converted YAML data to a file
        with open(output_file, 'w') as f:
            f.write(output_yaml)
        print(f"Configuration file created: {output_file}")
    else:
        print("Failed to convert YAML data.")
