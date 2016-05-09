class ShortStr;

class A{
public:
    int GetValue();
};

class B{
public:
    void Call(int);
};

class C{
public:
    void SetValue(int);
    ShortStr GetType();
};

class Foo{
public:
    ShortStr Bar(A a,B& b, C* c);
    int ma;
};
