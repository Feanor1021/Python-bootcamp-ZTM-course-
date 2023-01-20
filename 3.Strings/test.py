#C ile python arasında stringler konusunda bir bağ yok denebilir. Stringler burada ilk tanımda
#literaller bu *s="sea" string tanımı ile ortak. içinden herhangi bir şeyi değiştiremiyoruz.
#bu kullanımda 2 dilde benzer.
#Ama literal olmayan stringlerde büyük farklılıklar var
#burada char tipi yok o yüzden listler ile değişebilen string dizeleri yaratabiliyoruz
#ama char tipi olmadığı için her indise bir string de verebiliriz karakterden ziyade
#örneğin a=list("hello") da a[0]="mello" yaparsak melloello yazar h yerine mello koyar
#onun dışında başka bir değişken açıp bir string listine eşitlersek 2 listte aynı memory bloğunu gösterir bu açıdan c ile benzer
#ama a+1 gibi pointer aritmetikleri dilde yok yani bir stringin bir parçaşından itibaren başka bir pointer ile oraya erişme yok
#bunun yerine slicing dediğimiz [::] operatörü var bununla stringin istenilen her parçasına methodları da kullanarak erişebiliriz.
#örneğin a="hello" olsun bunun ello kısmını almak istiyoruz ama e'nin 1. indis olduğunu bilmiyoruz
#b=a[a.find('e'):] yazabiliriz ama bu işlem bize a helloyu gösterirken b de hellonun e'sinden itibaren
# point ediyor şeklinde düşündürmemeli slicing kopya oluşturur maalesef. bunu c de yapmak isteseydik e'yi bulmak için bir başka pointer daha açar base adresten itibaren
#a'yı itarete ederdik ama burada böyle bir şeye gerek duymuyoruz.
#Bu değişmezlik özelliğinin sebebi de pythonda her değişken pointer gibi bir şey
#özetle C deki gibi özgür bırakma yok burada her şeyi methodlar slicing v.s ile yapıyoruz.
#slicing de kopya oluşturuyor.

a=list("hello")

b=a[a.index('e'):]

a[1]='k'

print(b,a)