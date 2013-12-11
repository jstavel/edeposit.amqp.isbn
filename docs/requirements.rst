Požadavky na modul a jeho omezení
----------------------------------------------------------------------------------------------------

Požadavky na funkci modulu
...................................................

Požadavky které jsou kladeny na funkci systému.

#. modul kontroluje, zda je zadané ISBN validní
#. modul umí pracovat s ISBN-10 ISBN-13
#. modul umí poskytnout informaci o producentovi, který je v ISBN
   zakodovaný
#. modul umí poskytnout informaci, zda už bylo ISBN použito
#. modul umí poskytnout informaci o publikaci s daným ISBN
#. modul získává informace ze systému Aleph

Omezení systému
............................

#. middleware k implementaci využívá **RabbitMQ**, tj. je implementován odděleně od web rozhraní
#. middleware je napsaný v jazyce **Python**

