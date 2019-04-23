### **简要描述：**

复制{{model.name}}

### **请求URL：**

`/api/{{app_name | lower}}/{{model.name}}/<{{model.name}}_id>/`

### **请求方式：**

POST

### **类型：**

{% for field in model.field_list %}
{% if "enums" is in(field) %}
---
#### {{field.field_name}}
|值|原名|备注|
|:--|:--|:--|
{% for enum in field["enums"] %}
|{{ loop.index }}|{{enum["name"]}}||
{% endfor %}

{% endif %}
{% endfor %}

### **请求参数：**

|参数名|参数类型|备注|
|:--|:--|:--|
{% if "parent" in model and model["parent"] %}
{% for field in apps_dict[app_name][model["parent"]].field_list %}
|{{field.field_name}}|{{field.field_type}}|{{field.get("help_text", "")}}|
{% endfor %}
{% endif %}
{% for field in model.field_list %}
|{{field.field_name}}|{{field.field_type}}|{{field.get("help_text", "")}}|
{% endfor %}

[返回目录](../base.md)

