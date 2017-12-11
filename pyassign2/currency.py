def converse(currency_from, currency_to, amount_from):
    """converse input into url"""
    appendix = 'from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)
    url = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?' + appendix
    return url

def getjstr(url):
    """get string from url"""
    from urllib.request import urlopen
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def translate(jstr):
    """translate jstr into amount_to"""
    list1 = jstr.split()
    number = list1[list1.index('"to"')+2]
    amount_to = float(number[1:])
    return amount_to

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in
    currency currency_from to the currency currency_to. The value
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    url = converse(currency_from, currency_to, amount_from)
    jstr = getjstr(url)
    amount_to = translate(jstr)
    return(amount_to)

def test_A():
    """test converse()"""
    assert(converse("AED","LKR",10.0)=="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=AED&to=LKR&amt=10.0")
    assert(converse("MDL","MMK",0.1)=="http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=MDL&to=MMK&amt=0.1")

def test_B():
    """test getjstr()"""
    assert(getjstr("http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=AED&to=LKR&amt=10.0")=="""{ "from" : "10 United Arab Emirates Dirhams", "to" : "415.50739501829 Sri Lankan Rupees", "success" : true, "error" : "" }""")
    assert(getjstr("http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=MDL&to=MMK&amt=0.1")=="""{ "from" : "0.1 Moldovan Lei", "to" : "7.6729417681886 Myanma Kyats", "success" : true, "error" : "" }""")

def test_C():
    """test translate()"""
    assert(translate("""{"from" : "0.1 Moldovan Lei", "to" : "7.6729417681886 Myanma Kyats", "success" : true, "error" : "" }""")==7.6729417681886)

def test_D():
    """test exchange()"""
    assert(exchange("BGN","MRO",1.01)==224.88114099908)

def testAll():
    """test all cases"""
    test_A()
    test_B()
    test_C()
    test_D()
    print("All tests passsed")

testAll()
