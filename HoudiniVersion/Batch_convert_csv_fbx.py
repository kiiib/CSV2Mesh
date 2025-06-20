import os
import hou


# select the folder path
csv_folder_path = hou.ui.selectFile(
    start_directory="$HIP",
    title="Select the csv files folder path",
    file_type=hou.fileType.Directory
)
# csv_folder_path = r"D:\Projects\CSV2Mesh\TestSamples"

try:
    importer_node = hou.node("/obj/CSV2FBX/csv_importer")
    exporter_node = hou.node("/obj/CSV2FBX/fbx_exporter")

    if not importer_node or not exporter_node:
        raise Exception("Importer or exporter node not found")

except Exception as e:
    hou.ui.displayMessage(f"Error: {e}", severity=hou.severityType.Error)
    raise

print("----Batch conversion started----")

for filename in os.listdir(csv_folder_path):
    # only process csv files
    if filename.lower().endswith(".csv"):
        input_csv_path = f"{csv_folder_path}/{filename}"

        print(f"Processing {filename}...")

        # set varibles in nodes
        importer_node.parm("file").set(input_csv_path)

        exporter_node.render()

        print(f"Conversion complete for {filename}")

print("----Batch conversion completed----")
hou.ui.displayMessage("Batch conversion completed")