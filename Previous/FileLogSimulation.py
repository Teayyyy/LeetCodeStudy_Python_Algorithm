class File_Log_Simulation:
    def file_log(self, logs: [str]) -> int:
        # the depth of the folder layer, default by 0
        layer = 0
        for op in logs:
            if op[-2].isalpha() or op[-2].isnumeric():
                layer += 1
            elif op[-2] == '.':
                if len(op) >= 3 and op[-3] == '.':
                    layer = max(0, layer - 1)
        return layer



files = File_Log_Simulation()
print(files.file_log(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
