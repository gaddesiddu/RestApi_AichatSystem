def generate_ai_response(message):
    code = {
        "python": "print('Hello world')",
        "c++": (
            "#include <iostream>"
            "using namespace std;"
            "int main() {"
            "    cout << \"Hello World\" << endl;"
            "    return 0;"
            "}"
        ),
        "java": (
            "public class Hello {\n"
            "   public static void main(String[] args) {\n"
            "       System.out.println(\"Hello World\");\n"
            "   }\n"
            "}"
        ),
        "c": (
            "#include <stdio.h>\n"
            "int main() {\n"
            "   printf(\"Hello world\\n\");\n"
            "   return 0;\n"
            "}"
        ),
        "go": (
            "package main\n"
            "import \"fmt\"\n"
            "func main() {\n"
            "   fmt.Println(\"Hello World\")\n"
            "}"
        ),
    }

    for lang, code_snippet in code.items():
        if lang in message.lower():
            return f"Code for 'Hello World' in {lang}:{code_snippet}"
    
    return "Sorry, I could not generate 'Hello World' for your requested language."
