import markdown
import sys


args = sys.argv[1:] # file-comverter.py以下の引数の配列
argc = len(args) - 1 # 引数の数


# 引数の数を確認するバリデータ
def validate_argc(option, argc):
    if option != 'markdown' and argc != 2:
        print("Error: Invalid number of arguments.")
        sys.exit(1)

# 拡張子を確認するバリデータ
def validate_extension(inputfile, outputfile):
    if (not inputfile.endswith('.md') or not outputfile.endswith('.html')):
        print('Error: The file extension is different.')
        print("Hint: Specify the .md file as the first argument and the Specify an .html file as the second argument.")
        sys.exit(1)

def convert_markdown_to_html(inputfile, outputfile):
    with open(inputfile, 'r') as f:
        md_file = f.read()
    html = markdown.markdown(md_file)
    with open(outputfile, 'x') as f:
        f.write(html)


if (args[0] == 'markdown'):
    validate_argc(args[0], argc)
    validate_extension(args[1], args[2])
    convert_markdown_to_html(args[1], args[2])