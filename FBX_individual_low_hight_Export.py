import bpy
import os

# 出力フォルダを作成
output_dir = "/Users/horiuchi/Documents/FBX_export"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# シーン内のオブジェクトを取得
allobjects = bpy.context.scene.objects

# オブジェクトをループ処理
for i, obj in enumerate(allobjects):
    # 出力ファイル名を生成
    output_file_name = os.path.join(output_dir, f"{i:03}_{obj.name}" + "_hight" + ".fbx")

    object = bpy.data.objects[i]
    object.select_set(True)

    # FBXで書き出し
    bpy.ops.export_scene.fbx(
        filepath=output_file_name,
        check_existing=False,
        use_selection=True,
        use_mesh_modifiers=True,
    )
    
    bpy.ops.object.select_all(action='DESELECT')

    print(f"{i}番目のオブジェクト {obj.name} を {output_file_name} に書き出しました。")

for i, obj in enumerate(allobjects):
    # 出力ファイル名を生成
    output_file_name = os.path.join(output_dir, f"{i:03}_{obj.name}" + "_low" + ".fbx")

    object = bpy.data.objects[i]
    object.select_set(True)

    # FBXで書き出し
    bpy.ops.export_scene.fbx(
        filepath=output_file_name,
        check_existing=False,
        use_selection=True,
        use_mesh_modifiers=False,
    )    

    bpy.ops.object.select_all(action='DESELECT')
    
    print(f"{i}番目のオブジェクト {obj.name} を {output_file_name} に書き出しました。")
        