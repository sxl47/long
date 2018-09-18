# long




# qt 4.8
1.0 安装pyqt4.8 ……
1.1 增加ui模板
右键项目——新增——编辑文件模板——增加：
名字为：ui
模板代码为：
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>${NAME}</class>
 <widget class="QWidget" name="${NAME}">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>400</width>
    <height>300</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>${NAME}</string>
  </property>
 </widget>
 <resources/>
 <connections/>
</ui>

1.2 增加ui转py代码的工具
设置——工具——外部工具——增加：
（这里是qt4.x）
名字：uic4
描述：uic4 qt4的ui生成工具
program：C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat
argument：-o $FileNameWithoutAllExtensions$_ui.py $FileName$
working directory：$FileDir$

如果是qt5以上，则为：
名字：uic5
描述：uic5 qt5的ui生成工具
program：C:\Users\Administrator\AppData\Local\Programs\Python\Python35\Scripts\pyuic5.exe
argument：-o $FileNameWithoutAllExtensions$_ui.py $FileName$
working directory：$FileDir$
