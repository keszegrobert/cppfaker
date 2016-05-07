ShortStr Foo::Bar(A a,B& b, C* c)
{
    ma = a.GetValue();
    b.Call(ma);
    c->SetValue(0);
    return c->GetType() + ' ' + ShortStr(ma);
}