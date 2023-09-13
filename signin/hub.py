import asyncio
import subprocess
import os

from signin.test_login import run_script

os.system('cls')

async def execute_script(script_name, user, password):
    cmd = f"python {script_name} {user} {password}"
    process = await asyncio.create_subprocess_shell(cmd,stdout=asyncio.subprocess.PIPE)
    output, _ = await process.communicate()

    if output:
        print('--encontrado--')
        return output.decode(encoding='latin-1').strip()
    else:
        print('-- NOencontrado--')
        return ''

async def main(user,passwd):

    script_test_login = await run_script(user, passwd)

    if script_test_login == "OK" :

        tasksPa = []
        tasksMe = []
        results=[]

        tasksPa.append(await execute_script('signin\pa.py', user, passwd))
        tasksMe.append(await execute_script('signin\me.py', user, passwd))

        for x in range(len(tasksPa)):
            results.append(tasksPa[x])

        for y in range(len(tasksMe)):
            results.append(tasksMe[y])

        return results

if __name__ == "__main__":
    asyncio.run(main())