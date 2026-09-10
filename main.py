"""Executa os downloads em sequência no Windows. Use: python main.py"""
from pathlib import Path
import subprocess
import sys

PASTA = Path(__file__).resolve().parent
SCRIPTS = ['IAD.py', 'TCL.py']  # Acrescente novas automações aqui.
TIMEOUT = 1800  # 30 minutos por script, incluindo seus quatro graus.


def main():
    falhas = []
    for script in SCRIPTS:
        print(f'Iniciando {script}', flush=True)
        try:
            with (PASTA / f'{Path(script).stem}.log').open('w', encoding='utf-8') as log:
                processo = subprocess.Popen(
                    [sys.executable, '-u', str(PASTA / script)],
                    cwd=PASTA, stdout=log, stderr=subprocess.STDOUT,
                    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP,
                )
                try:
                    codigo = processo.wait(timeout=TIMEOUT)
                except (subprocess.TimeoutExpired, KeyboardInterrupt):
                    # Windows: encerra também o navegador iniciado pelo script.
                    if processo.poll() is None:
                        try:
                            subprocess.run(
                                ['taskkill', '/PID', str(processo.pid), '/T', '/F'],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                check=True, timeout=20,
                            )
                        except (OSError, subprocess.SubprocessError):
                            print('Não foi possível encerrar o processo. Execução cancelada.', flush=True)
                            return 1
                    processo.wait()
                    raise
            if codigo != 0:
                falhas.append(script)
                print(f'Falha em {script}. Veja o arquivo .log.', flush=True)
            else:
                print(f'{script} concluído.', flush=True)
        except KeyboardInterrupt:
            print('Execução interrompida.', flush=True)
            return 1
        except (OSError, subprocess.SubprocessError) as erro:
            falhas.append(script)
            print(f'Falha em {script}: {erro}', flush=True)
    print('Finalizado. Falhas: ' + (', '.join(falhas) or 'nenhuma'), flush=True)
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
