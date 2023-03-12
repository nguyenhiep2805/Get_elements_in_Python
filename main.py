import ezdxf
import pandas as pd
from convert import dwg_to_dxf
from delete import delete_file, delete_folder

# [========== XỬ LÍ BẢN VẼ ==========]
# Convert file .dwg sang .dxf
input_folder = r"D:\Study\Program\Python\For AutoCAD\Code"
output_folder = input_folder
dwg_to_dxf(input_folder, output_folder)

# Load file dxf
dwg = ezdxf.readfile("Ban_ve.dxf")

# [========== ĐƯỜNG TRÒN ==========]
# Lấy tất cả các đường tròn trong bản vẽ
circles = dwg.modelspace().query('CIRCLE')

# Tạo DataFrame từ danh sách các đường tròn
circle_data = []
for circle in circles:
    center = circle.dxf.center
    radius = circle.dxf.radius
    circle_data.append((center[0], center[1], radius))
# Tạo DataFrame từ danh sách điểm và đường kính
circle_df = pd.DataFrame(circle_data, columns=['X', 'Y', 'Radius'])

# [========== ĐOẠN THẲNG ==========]
# Lấy tất cả các đoạn thẳng trong bản vẽ
lines = dwg.modelspace().query('LINE')

# Tạo DataFrame từ danh sách các đoạn thẳng
line_data = []
for line in lines:
    start = line.dxf.start
    end = line.dxf.end
    line_data.append((start[0], start[1], end[0], end[1]))
# Tạo DataFrame từ danh sách điểm
line_df = pd.DataFrame(line_data, columns=['X1', 'Y1', 'X2', 'Y2'])

# [========== SPLINE ==========]
# Lấy tất cả các spline trong bản vẽ
splines = dwg.modelspace().query('SPLINE')
# Tạo danh sách các điểm thuộc các spline
spline_data = []
for spline in splines:
    points = spline.fit_points
    for point in points:
        spline_data.append((spline.dxf.handle, point[0], point[1]))
# Tạo DataFrame từ danh sách điểm
spline_df = pd.DataFrame(spline_data, columns=['Spline', 'X', 'Y'])

# [========== GHI DATAFRAME VÀO FILE EXCEL ==========]
with pd.ExcelWriter('data.xlsx') as writer:
    circle_df.to_excel(writer, sheet_name='Circle', index=False)
    line_df.to_excel(writer, sheet_name='Line', index=False)
    spline_df.to_excel(writer, sheet_name='Spline', index=False)
print('Da nhap du lieu vao file data.xlsx')

# [========== XOÁ FILE/ FOLDER KHÔNG CẦN THIẾT ==========]
delete_file('Ban_ve.dxf')
delete_folder('__pycache__')
delete_folder('.idea')