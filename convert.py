import subprocess


def dwg_to_dxf(input_folder, output_folder):
    # Define parameters
    teigha_path = r"C:\Program Files\ODA\ODAFileConverter 24.1.0\ODAFileConverter.exe"
    outver = "ACAD2018"
    outformat = "DXF"
    recursive = "0"
    audit = "1"
    input_filter = "*.DWG"

    # Define command
    cmd = [
        teigha_path,
        input_folder,
        output_folder,
        outver,
        outformat,
        recursive,
        audit,
        input_filter,
    ]

    # Run command
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1, universal_newlines=True, shell=True) as proc:
        for line in proc.stdout:
            print(line, end="")


# Completed
print('Da convert file Ban_ve.dwg thanh file Ban_ve.dxf')
