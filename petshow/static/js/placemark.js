// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.
ymaps.ready(init);

function init() {
  var myMap = new ymaps.Map(
      "map",
      {
        center: [55.765767, 37.685611],
        zoom: 16,
      },
      {
        searchControlProvider: "yandex#search",
      },
    ),
    // Создаем геообъект с типом геометрии "Точка".
    myGeoObject = new ymaps.GeoObject(
      {
        // Описание геометрии.
        geometry: {
          type: "Point",
          coordinates: [55.7887683, 37.79149103],
        },
        // Свойства.
        properties: {
          // Контент метки.
          iconContent: "Я тащусь",
          hintContent: "Ну давай уже тащи",
        },
      },
      {
        // Опции.
        // Иконка метки будет растягиваться под размер ее содержимого.
        preset: "islands#blackStretchyIcon",
        // Метку можно перемещать.
        draggable: true,
      },
    ),
    myPieChart = new ymaps.Placemark(
      [55.847, 37.6],
      {
        // Данные для построения диаграммы.
        data: [
          { weight: 8, color: "#0E4779" },
          { weight: 6, color: "#1E98FF" },
          { weight: 4, color: "#82CDFF" },
        ],
        iconCaption: "Диаграмма",
      },
      {
        // Зададим произвольный макет метки.
        iconLayout: "default#pieChart",
        // Радиус диаграммы в пикселях.
        iconPieChartRadius: 30,
        // Радиус центральной части макета.
        iconPieChartCoreRadius: 10,
        // Стиль заливки центральной части.
        iconPieChartCoreFillStyle: "#ffffff",
        // Cтиль линий-разделителей секторов и внешней обводки диаграммы.
        iconPieChartStrokeStyle: "#ffffff",
        // Ширина линий-разделителей секторов и внешней обводки диаграммы.
        iconPieChartStrokeWidth: 3,
        // Максимальная ширина подписи метки.
        iconPieChartCaptionMaxWidth: 200,
      },
    );

  myMap.geoObjects.add(
    new ymaps.Placemark(
      [55.765767, 37.685611],
      {
        balloonContent: "Наш офис",
      },
      {
        preset: "islands#redDotIconWithCaption",
      },
    ),
  );
}
