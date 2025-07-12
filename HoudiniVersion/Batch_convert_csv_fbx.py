import os
import hou

#csv_folder_path = r"D:\Projects\CSV2Mesh\TestSamples"
try:
    param_controller_node = hou.node("/obj/CSV2FBX/parameters_controller")
    
    if param_controller_node is None:
        raise Exception("parameters controller node not found")
        
    csv_folder_path = param_controller_node.parm('csv_folder_path').eval()
    fbx_folder_path = param_controller_node.parm('fbx_folder_path').eval()
    print(csv_folder_path)
    print(fbx_folder_path)
    
    if not csv_folder_path or not fbx_folder_path:
        raise Exception("Please set both the CSV and FBX folder path on the 'parameters_controller'")
        
except Exception as e:
    hou.ui.displayMessage(f"Error: {e}", severity=hou.severityType.Error)
    raise

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
        exporter_node.parm("sopoutput").set(fbx_folder_path + "/" + filename.replace(".csv", ".fbx"))

        exporter_node.render()

        print(f"Conversion complete for {filename}")

print("----Batch conversion completed----")
hou.ui.displayMessage("Batch conversion completed")