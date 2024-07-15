# autotool
主要用于做桌面自动化操作的工具

# 打包流程
1、pyinstaller --onefile --add-data "./data;." main.py zombie.py general_operation.py
   该步骤可以生成：./dist/main.exe

2、直接运行exe会报错：ModuleNotFoundError: No module named 'comtypes.stream'
   在另一个打包时生成的文件：main.spec 里，hiddenimports字段后面添加'comtypes.stream'，如果有多个，用逗号隔开即可。然后再执行：pyinstaller .\main.spec，再次生成的exe文件就可以正确执行了