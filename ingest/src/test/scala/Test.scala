
import org.scalatest._

class test extends FunSuite  with Matchers {
 // Pour les tests on a pas de fonction à tester, mais la structure de teste marche bien.
  val sysdate :String = "2020-12-13"

  test("test sysDate "){
    sysdate should be ("2020-12-13")
  }
}


