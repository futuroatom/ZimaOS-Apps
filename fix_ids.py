import os
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True

apps_dir = "Apps"

if os.path.exists(apps_dir):
    for app_name in os.listdir(apps_dir):
        app_path = os.path.join(apps_dir, app_name)
        compose_file = os.path.join(app_path, "docker-compose.yml")
        
        if os.path.isfile(compose_file):
            try:
                with open(compose_file, "r", encoding="utf-8") as f:
                    data = yaml.load(f)
                
                if data and "x-casaos" in data:
                    # Gera um ID de domínio reverso baseado no nome da pasta do app
                    clean_name = app_name.lower().replace("_", "-").replace(".", "")
                    reverse_id = f"com.zimaos.{clean_name}"
                    
                    # Atualiza o ID
                    data["x-casaos"]["id"] = reverse_id
                    
                    with open(compose_file, "w", encoding="utf-8") as f:
                        yaml.dump(data, f)
                    print(f"Atualizado: {app_name} -> {reverse_id}")
            except Exception as e:
                print(f"Erro ao processar {app_name}: {e}")
