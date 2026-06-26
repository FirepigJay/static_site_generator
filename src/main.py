import os, shutil
from markdown_blocks import markdown_to_html_node

def copy_folder_and_files(source_directory, destination_directory) -> None:
    if os.path.exists(destination_directory):
        shutil.rmtree(destination_directory)
        
    os.mkdir(destination_directory)

    
    folders_and_files = os.listdir(source_directory)
    for folder_file in folders_and_files:
        source_filepath = os.path.join(source_directory, folder_file)
        destination_filepath = os.path.join(destination_directory, folder_file)
        if os.path.isfile(source_filepath):
            shutil.copy(source_filepath, destination_filepath)
        else:
            copy_folder_and_files(source_filepath,destination_filepath)
    
def extract_title(markdown:str) -> str:
    lines = markdown.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:]
    raise Exception('no Title found')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    from_path_content = ''
    template_path_content = ''
    with open(from_path, 'r') as file:
        from_path_content = file.read()
    with open(template_path, 'r') as file:
        template_path_content = file.read()
    content = markdown_to_html_node(from_path_content)
    print(content)
    content = content.to_html()
    title = extract_title(from_path_content)
    template_path_content = template_path_content.replace('{{ Title }}', title)
    template_path_content = template_path_content.replace('{{ Content }}', content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(template_path_content)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files_or_folders = os.listdir(dir_path_content)
    for file_or_folder in files_or_folders:
        complete_path = os.path.join(dir_path_content, file_or_folder)
        dest_path = os.path.join(dest_dir_path,file_or_folder.replace('.md', '.html'))
        if os.path.isfile(complete_path):
            generate_page(complete_path, template_path, dest_path)
        else:
            generate_pages_recursive(complete_path, template_path, dest_path)


def main():
    script_path = os.path.abspath(__file__)
    parent_path = os.path.dirname(script_path)
    base_dir = os.path.dirname(parent_path)

    source_dir = os.path.join(base_dir, 'static')
    destination_dir = os.path.join(base_dir, 'public')
    copy_folder_and_files(source_dir, destination_dir)

    # generate_page(from_path='content/index.md', template_path='template.html', dest_path='public/index.html')
    # generate_page(from_path='content/blog/glorfindel/index.md', template_path='template.html', dest_path='public/blog/glorfindel/index.html')
    # generate_page(from_path='content/blog/majesty/index.md', template_path='template.html', dest_path='public/blog/majesty/index.html')
    # generate_page(from_path='content/blog/tom/index.md', template_path='template.html', dest_path='public/blog/tom/index.html')
    generate_pages_recursive(dir_path_content='content', template_path='template.html', dest_dir_path='public')

main()