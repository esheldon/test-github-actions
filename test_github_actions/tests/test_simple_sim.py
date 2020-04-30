from descwl_shear_sims import Sim


def test_simple_sim_smoke():
    sim = Sim(rng=10, gals_kws={'density': 10})
    _ = sim.gen_sim()
