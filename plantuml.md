# PlantUML

- To run locally: `java -jar plantuml-jar-file.jar diagram.txt`
- List all fonts
```
@startuml
listfonts
@enduml
```
- Legend
```
legend right
  |Prop|Val|
endlegend
```
- [Creole text-formatting](https://plantuml.com/creole)
- Dashed rectangle
```
@startuml
rectangle "Rectangle" as RectangleName
rectangle "Dashed-Rectangle" as DashedRectangleName #line.dashed
@enduml
```
