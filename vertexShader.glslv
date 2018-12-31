#version 430 core

in vec3 vPosition;
in vec2 texCoords;

out vec2 pass_texCoords;

uniform mat4  transforMatrix = mat4(1.0);
uniform float uniScale       = 1.0;

void
main() {
    gl_Position = transforMatrix * vec4( vPosition, 1.0/uniScale );
    pass_texCoords = texCoords;
    }

