import subprocess
import sys

# Source: https://junegunn.github.io/fzf/tips/using-fzf-in-your-program/#python
def with_filter(command, work):
    process = subprocess.Popen(
        command, 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        text=True, 
        shell=True
    )
    original_stdout = sys.stdout
    sys.stdout = process.stdin
    try:
        work()
        process.stdin.close()
    except:
        pass
    finally:
        sys.stdout = original_stdout

    output = process.stdout.read().splitlines()
    process.stdout.close()
    return output

def fzf(function) -> str:
    """Provide fzf with function called"""
    # !NOTE When using fzf, rich cannot keep the ANSI format to output formated result
    try:
        return with_filter(r'fzf --reverse --height 60%', function)[0]
    except IndexError:
        pass

if __name__ == '__main__':
    from rich import print
    
    def hello():
        for i in range(10):
            print(i, flush=True)
    answer = fzf(hello)
    if answer:
        print(answer)
        print(f'[red]{answer}[/red]')