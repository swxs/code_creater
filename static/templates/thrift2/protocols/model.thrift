struct CreateResult {
    1: required i32 code;
    2: optional string id;
    3: optional string msg;
}

struct UpdateResult {
    1: required i32 code;
    2: optional string id;
    3: optional string msg;
}

struct DeleteResult {
    1: required i32 code;
    2: optional string msg;
}

{% for model_name, model in models.items() %}
struct {{model_name | title}} {
    1: optional string id;
    {% for field in model.field_list %}
        {% if field.field_type == "datetime" %}
    {{loop.index+1}}: optional string {{field.field_name}};
        {% elif field.field_type == "str" %}
    {{loop.index+1}}: optional string {{field.field_name}};
        {% elif field.field_type == "int" %}
    {{loop.index+1}}: optional i32 {{field.field_name}};
        {% elif field.field_type == "list" %}
            {% if field.field_detail_type == "str" %}
    {{loop.index+1}}: optional list<string> {{field.field_name}};
            {% elif field.field_detail_type == "int" %}
    {{loop.index+1}}: optional list<inting> {{field.field_name}};
            {% elif field.field_detail_type == "objectid" %}
    {{loop.index+1}}: optional list<string> {{field.field_name}};
            {% elif field.field_detail_type == "dict" %}
    {{loop.index+1}}: optional list<string> {{field.field_name}};
            {% else %}
    {{loop.index+1}}: optional list<string> {{field.field_name}};
            {% endif %}
        {% elif field.field_type == "dict" %}
    {{loop.index+1}}: optional string {{field.field_name}};
        {% elif field.field_type == "boolean" %}
    {{loop.index+1}}: optional bool {{field.field_name}};
        {% elif field.field_type == "objectid" %}
    {{loop.index+1}}: optional string {{field.field_name}};
        {% else %}
    {{loop.index+1}}: optional string {{field.field_name}};
        {% endif %}
    {% endfor %}
}

struct {{model_name | title}}Result {
    1: required i32 code;
    2: optional {{model_name}} {{model_name | lower}};
    3: optional string msg;
}

typedef list<{{model_name | title}}> {{model_name | title}}List

struct {{model_name | title}}SearchResult {
    1: required i32 code;
    2: optional {{model_name | title}}List {{model_name | lower}}_list;
    3: optional string msg;
}

{% endfor %}

service {{app_name | title}}Service {
    {% for model_name, model in models.items() %}
    CreateResult create_{{app_name | lower}}_{{model_name | lower}}(1:{{model_name}} {{model_name | lower}}),
    UpdateResult update_{{app_name | lower}}_{{model_name | lower}}(1:{{model_name}} {{model_name | lower}}),
    DeleteResult delete_{{app_name | lower}}_{{model_name | lower}}(1:list<string> idList),
    {{model_name}}Result select_{{app_name | title}}_{{model_name|lower}}(1: string oid),
    {{model_name}}SearchResult search_{{app_name | title}}_{{model_name | lower}}(),
    {% endfor %}
}
