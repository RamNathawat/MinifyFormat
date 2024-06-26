import os
import jsbeautifier
import autopep8
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_minified(content):
    lines = content.split('\n')
    average_line_length = sum(len(line) for line in lines) / max(len(lines), 1)
    long_lines = sum(1 for line in lines if len(line) > 200)
    return average_line_length > 200 or long_lines > 0.5 * len(lines)

def format_js(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return

    if is_minified(content):
        logging.info(f"Formatting minified JavaScript file: {file_path}")
        opts = jsbeautifier.default_options()
        opts.indent_size = 4
        beautified_content = jsbeautifier.beautify(content, opts)

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(beautified_content)
        except Exception as e:
            logging.error(f"Error writing to file {file_path}: {e}")

def format_python(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return

    if is_minified(content):
        logging.info(f"Formatting minified Python file: {file_path}")
        beautified_content = autopep8.fix_code(content)

        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(beautified_content)
        except Exception as e:
            logging.error(f"Error writing to file {file_path}: {e}")

def format_files_in_folder(folder_path):
    start_time = time.time()
    formatted_files_count = 0
    total_files_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_start_time = time.time()
            if file.endswith('.js'):
                format_js(file_path)
                formatted_files_count += 1
            elif file.endswith('.py'):
                format_python(file_path)
                formatted_files_count += 1
            file_end_time = time.time()
            logging.info(f"Formatted {file_path} in {file_end_time - file_start_time:.2f} seconds")
            total_files_count += 1
    end_time = time.time()
    logging.info(f"Total files formatted: {formatted_files_count}/{total_files_count}")
    logging.info(f"Total time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing minified code: ").strip()
    if os.path.isdir(folder_path):
        format_files_in_folder(folder_path)
        logging.info("Formatting completed.")
    else:
        logging.error("The provided path is not a valid folder.")
