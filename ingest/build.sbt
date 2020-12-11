name := "ingest"

version := "0.1"

scalaVersion := "2.12.12"

lazy val commonSettings = Seq(
  organization := "poc.talenthunter",
  version := "1.0",
  scalaVersion := "2.12.12",
  libraryDependencies ++= Seq(
    "com.typesafe" % "config" % "1.4.0",
    "org.jmockit" % "jmockit" % "1.34" % "test",
    "org.slf4j" % "slf4j-api" % "1.7.25",
    "org.apache.spark" % "spark-core_2.12" % "2.4.4",
    "org.apache.spark" % "spark-sql_2.12" % "2.4.4",
    "org.elasticsearch" % "elasticsearch-hadoop" % "7.1.0",
    "org.antlr" % "antlr4-runtime" % "4.7.2"
  )

)

lazy val Project = (project in file("."))
  .settings(commonSettings)


assemblyMergeStrategy in assembly := {
  case PathList("META-INF", xs @ _*) => MergeStrategy.discard
  case x => MergeStrategy.first
}
