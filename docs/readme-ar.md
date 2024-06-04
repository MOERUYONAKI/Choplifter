# Choplifter

## I - الاحتياجات

**Python 3** أو أحدث
> مكتبة "**Pygame 2.5.0**"  
> حزمة "**PyInstaller 6.7.0**"  
  
## II - أوامر CHPrompt

**1 - /clear**  
> يفرغ CHPrompt  
  
**2 - /exit**  
> يغلق CHPrompt  
  
**3 - /help**  
> يعرض قائمة الأوامر 
  
**4 - /play** *[ -f ]* *[ -s ]*  
> يشغل Choplifter  
> [ -f ] - وضع الشاشة الكاملة *(تجريبي)*  
> [ -s ] - وضع البقاء على قيد الحياة 
  
**5 - /repo**  
> يرجع رابط المستودع  
  
## III - اللعبة  
  
### مقدمة
  
> لعبة *Choplifter* هي محاكاة لإنقاذ الرهائن باستخدام مروحية، حيث يجب على اللاعب تجنب الأعداء وإنقاذ أكبر عدد ممكن من الرهائن. تتطلب هذه اللعبة Python ومكتبة Pygame.  
  
### منطق اللعبة
  
> **التهيئة**: إعداد نافذة اللعبة، تحميل الصور، وتهيئة متغيرات اللعبة.  
> **الحلقة الرئيسية**: إدارة إدخالات اللاعب، تحديث حالة اللعبة، وعرض الرسومات.  
> **إدارة التصادمات**: كشف التصادمات بين المروحية والأعداء والرهائن والقذائف لإدارة التفاعلات.  
> **إنقاذ الرهائن**: يجب على المروحية الهبوط بالقرب من الرهائن لإنقاذهم. يتجه الرهائن نحو المروحية عندما تكون في الأرض.  
> **نهاية اللعبة**: تنتهي اللعبة عند إنقاذ جميع الرهائن أو تدمير المروحية.  
  
### عناصر اللعبة
  
> **المروحية**: مركبة اللاعب. يمكنها التحرك في جميع الاتجاهات وإطلاق القذائف.  
> **الأعداء**: الدبابات والطائرات النفاثة والكائنات الفضائية التي تحاول تدمير المروحية.  
> **الرهائن**: المدنيون الذين يجب إنقاذهم. يتحركون نحو المروحية عندما تهبط.  
> **القاعدة**: الهياكل التي يتم تحديد موقع الرهائن فيها في البداية.  
> **القذائف**: يتم إطلاقها بواسطة المروحية للتخلص من الأعداء.  
  
### نهاية اللعبة
  
> تنتهي اللعبة عند إنقاذ جميع الرهائن أو تدمير المروحية. يتم عرض النقاط النهائية، استنادًا إلى عدد الرهائن المنقذين والأعداء المدمرين، على الشاشة.  
  
## IV - المطورين
  
> [MOERUYONAKI](https://www.github.com/MOERUYONAKI)  
> [Kevin-Sawyer](https://www.github.com/Kevin-Sawyer)  
  