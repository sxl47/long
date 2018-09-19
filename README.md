# long


# pyqt
1. 安装pyqt4.8 ……
2. 增加ui模板  
- 右键项目—新增—编辑文件模板—增加：  
名字为：ui  
模板代码为：
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;ui version=&quot;4.0&quot;&gt;
 &lt;class&gt;${NAME}&lt;/class&gt;
 &lt;widget class=&quot;QWidget&quot; name=&quot;${NAME}&quot;&gt;
  &lt;property name=&quot;geometry&quot;&gt;
   &lt;rect&gt;
    &lt;x&gt;0&lt;/x&gt;
    &lt;y&gt;0&lt;/y&gt;
    &lt;width&gt;400&lt;/width&gt;
    &lt;height&gt;300&lt;/height&gt;
   &lt;/rect&gt;
  &lt;/property&gt;
  &lt;property name=&quot;windowTitle&quot;&gt;
   &lt;string&gt;${NAME}&lt;/string&gt;
  &lt;/property&gt;
 &lt;/widget&gt;
 &lt;resources/&gt;
 &lt;connections/&gt;
&lt;/ui&gt;
</pre>

3. 增加ui转py代码的工具
- 设置—工具—外部工具—增加：  
	1. 这里是qt4.x, 为：  
名字：uic4  
描述：uic4 qt4的ui生成工具  
program：C:\Python27\Lib\site-packages\PyQt4\pyuic4.bat  
argument：-o $FileNameWithoutAllExtensions$_ui.py $FileName$  
working directory：$FileDir$  
	2. 如果是qt5以上，则为：  
名字：uic5  
描述：uic5 qt5的ui生成工具  
program：C:\Users\Administrator\AppData\Local\Programs\Python\Python35\Scripts\pyuic5.exe  
argument：-o $FileNameWithoutAllExtensions$_ui.py $FileName$  
working directory：$FileDir$  

