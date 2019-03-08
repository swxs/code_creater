### **简要描述：**

创建{{app.name}}

### **请求URL：**

`/api/{{app.name}}/create/`

### **请求方式：**

POST

### **类型：**

### **请求参数：**

|参数名|参数类型|备注|
|:--|:--|:--|
{% for field in app.settings %}
|{{field.name}}|{{field.type}}|{{field.get('params', {}).get("help_text", "")}}|
{% endfor %}
