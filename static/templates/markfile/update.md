### **简要描述：**

更新{{app.name}}

### **请求URL：**

`/api/{{app.name}}/update/<{{app.name}}_id>`

### **请求方式：**

PATCH

### **类型：**

### **请求参数：**

|参数名|参数类型|备注|
|:--|:--|:--|
{% for field in app.settings %}
|{{field.name}}|{{field.type}}|{{field.get('params', {}).get("help_text", "")}}|
{% endfor %}