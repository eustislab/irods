import configuration
        self.admin.assert_icommand("iinit -l", 'STDOUT_SINGLELINE', self.admin.username)
        self.admin.assert_icommand("iinit -l", 'STDOUT_SINGLELINE', self.admin.zone_name)
        self.admin.assert_icommand("iinit -l", 'STDOUT_SINGLELINE', self.admin.default_resource)
        self.admin.assert_icommand("ilsresc", 'STDOUT_SINGLELINE', self.testresc)
        self.admin.assert_icommand("ilsresc -l", 'STDOUT_SINGLELINE', self.testresc)
        self.admin.assert_icommand("imiscsvrinfo", 'STDOUT_SINGLELINE', ["relVersion"])
        self.admin.assert_icommand("iuserinfo", 'STDOUT_SINGLELINE', "name: " + username)
        self.admin.assert_icommand("ienv", 'STDOUT_SINGLELINE', "irods_zone_name")
        self.admin.assert_icommand("ipwd", 'STDOUT_SINGLELINE', "home")
        self.admin.assert_icommand("ihelp ils", 'STDOUT_SINGLELINE', "ils")
        self.admin.assert_icommand("ierror -14000", 'STDOUT_SINGLELINE', "SYS_API_INPUT_ERR")
        self.admin.assert_icommand("iexecmd hello", 'STDOUT_SINGLELINE', "Hello world")
        self.admin.assert_icommand("ips -v", 'STDOUT_SINGLELINE', "ips")
        self.admin.assert_icommand("iqstat", 'STDOUT_SINGLELINE', "No delayed rules pending for user " + self.admin.username)
        self.admin.assert_icommand("ils -AL", 'STDOUT_SINGLELINE', "home")  # debug
        self.admin.assert_icommand("ichksum -f " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', "performed = 1")
        self.admin.assert_icommand("ils " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', "foo1")
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', ["foo1", myssize])
        self.admin.assert_icommand("iadmin ls " + irodshome + "/icmdtest", 'STDOUT_SINGLELINE', "foo1")
                   'STDOUT_SINGLELINE', username + "#" + irodszone + ":own")
                   'STDOUT_SINGLELINE', testuser1 + "#" + irodszone + ":read")
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', self.testresc)
        self.admin.assert_icommand_fail("ils -L " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', [irodsdefresource])
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', irodsdefresource[0:19])
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', ["testmeta1"])
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', ["180"])
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', ["cm"])
        self.admin.assert_icommand("ils " + irodshome + "/icmdtest/foo2", 'STDOUT_SINGLELINE', "foo2")
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest/foo4", 'STDOUT_SINGLELINE', "foo4")
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest/foo2", 'STDOUT_SINGLELINE', "foo2")
        self.admin.assert_icommand("ichksum " + irodshome + "/icmdtest/foo2", 'STDOUT_SINGLELINE', "foo2")
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', ["testmeta1"])
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', ["hello"])
        self.admin.assert_icommand("imeta qu -d testmeta1 = 180", 'STDOUT_SINGLELINE', "foo1")
        self.admin.assert_icommand("imeta qu -d testmeta2 = hello", 'STDOUT_SINGLELINE', "dataObj: foo1")
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', ["foo1", myssize])
                   'STDOUT_SINGLELINE', ["foo1", str(os.stat(sfile2).st_size)])
        self.admin.assert_icommand_fail("ils -l " + irodshome + "/icmdtest/foo1", 'STDOUT_SINGLELINE', myssize)
        self.admin.assert_icommand("iput -bIvPKr " + mysdir + " " + irodshome + "/icmdtest", 'STDOUT_SINGLELINE', "Bulk upload")
                   mysdir + " " + irodshome + "/icmdtestw", 'STDOUT_SINGLELINE', "Processing")
        self.admin.assert_icommand("ils -lr " + irodshome + "/icmdtestw1", 'STDOUT_SINGLELINE', "sfile10")
        self.admin.assert_icommand("ils -Ar " + irodshome + "/icmdtestw1", 'STDOUT_SINGLELINE', "sfile10")
        self.admin.assert_icommand("irm -rvf " + irodshome + "/icmdtestw1", 'STDOUT_SINGLELINE', "num files done")
                   irodshome + "/icmdtest " + dir_w + "/testx", 'STDOUT_SINGLELINE', "opened")
        self.admin.assert_icommand("ils -lr " + irodshome + "/icmdtestx", 'STDOUT_SINGLELINE', ["foo2"])
        self.admin.assert_icommand("ils -lr " + irodshome + "/icmdtestx", 'STDOUT_SINGLELINE', ["sfile10"])
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtestx1.tar", 'STDOUT_SINGLELINE', "testx1.tar")
        # test ibun with zip
        self.admin.assert_icommand("ibun -cDzip " + irodshome + "/icmdtestx1.zip " + irodshome + "/icmdtestx")
        self.admin.assert_icommand("ibun -x " + irodshome + "/icmdtestx1.zip " + irodshome + "/icmdtestzip")
        if os.path.isfile("icmdtestzip"):
            os.unlink("icmdtestzip")
        self.admin.assert_icommand("iget -vr " + irodshome + "/icmdtestzip " + dir_w + "", 'STDOUT_SINGLELINE', "icmdtestzip")
        output = commands.getstatusoutput("diff -r " + dir_w + "/testx " + dir_w + "/icmdtestzip/icmdtestx")
        print "output is [" + str(output) + "]"
        assert output[0] == 0
        assert output[1] == "", "diff output was not empty..."
        shutil.rmtree(dir_w + "/icmdtestzip")
        self.admin.assert_icommand("ibun --add " + irodshome + "/icmdtestx1.zip " + irodshome + "/icmdtestzip")
        self.admin.assert_icommand("irm -rf " + irodshome + "/icmdtestx1.zip " + irodshome + "/icmdtestzip")

        self.admin.assert_icommand("iget -vr " + irodshome + "/icmdtestgz " + dir_w + "", 'STDOUT_SINGLELINE', "icmdtestgz")
        self.admin.assert_icommand("iget -vr " + irodshome + "/icmdtestbz2 " + dir_w + "", 'STDOUT_SINGLELINE', "icmdtestbz2")
        self.admin.assert_icommand("itrim -N1 -S " + self.testresc + " -r " + irodshome + "/icmdtestbz2", 'STDOUT_SINGLELINE', "Total size trimmed")
        self.admin.assert_icommand("itrim -N1 -S " + irodsdefresource + " -r " + irodshome + "/icmdtestbz2", 'STDOUT_SINGLELINE', "Total size trimmed")
        self.admin.assert_icommand("ils --bundle " + bunfile, 'STDOUT_SINGLELINE', "Subfiles")
        self.admin.assert_icommand("iget -fvrK " + irodshome + "/icmdtesta " + dir_w + "/testa", 'STDOUT_SINGLELINE', "testa")
                   testuser2home + "/foo5", 'STDERR_SINGLELINE', "PATH_REG_NOT_ALLOWED")
        self.admin.assert_icommand("ils -lr " + irodshome + "/icmdtestb", 'STDOUT_SINGLELINE', "icmdtestb")
        self.admin.assert_icommand("iget -fvrK " + irodshome + "/icmdtestb " + dir_w + "/testb", 'STDOUT_SINGLELINE', "testb")
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest/foo100", 'STDOUT_SINGLELINE', "foo100")
        self.admin.assert_icommand("ils -lr " + irodshome + "/icmdtest/testmm1", 'STDOUT_SINGLELINE', "foo11")
        self.admin.assert_icommand("iget -fvrK " + irodshome + "/icmdtesta " + dir_w + "/testm", 'STDOUT_SINGLELINE', "testm")
        self.admin.assert_icommand("ils -lr " + irodshome + "/icmdtestt_mcol", 'STDOUT_SINGLELINE', ["foo2"])
        self.admin.assert_icommand("ils -lr " + irodshome + "/icmdtestt_mcol", 'STDOUT_SINGLELINE', ["foo1"])
        self.admin.assert_icommand("iget -vr " + irodshome + "/icmdtest  " + dir_w + "/testx", 'STDOUT_SINGLELINE', "testx")
                   "/icmdtestt_mcol/icmdtest  " + dir_w + "/testt", 'STDOUT_SINGLELINE', "testt")
                   irodshome + "/icmdtestp", 'STDOUT_SINGLELINE', "files trimmed")
                   irodshome + "/icmdtestp", 'STDOUT_SINGLELINE', "files trimmed")
        self.admin.assert_icommand("ils " + bunfile, 'STDOUT_SINGLELINE', bunfile)
        self.admin.assert_icommand("irm -rvf " + irodshome + "/icmdtestp", 'STDOUT_SINGLELINE', "num files done")
        self.admin.assert_icommand("ilsresc", 'STDOUT_SINGLELINE', self.testresc)
        self.admin.assert_icommand("imiscsvrinfo", 'STDOUT_SINGLELINE', "relVersion")
        self.admin.assert_icommand("iuserinfo", 'STDOUT_SINGLELINE', "name: " + username)
        self.admin.assert_icommand("ienv", 'STDOUT_SINGLELINE', "Release Version")
        self.admin.assert_icommand("ipwd", 'STDOUT_SINGLELINE', "home")
        self.admin.assert_icommand("ihelp ils", 'STDOUT_SINGLELINE', "ils")
        self.admin.assert_icommand("ierror -14000", 'STDOUT_SINGLELINE', "SYS_API_INPUT_ERR")
        self.admin.assert_icommand("iexecmd hello", 'STDOUT_SINGLELINE', "Hello world")
        self.admin.assert_icommand("ips -v", 'STDOUT_SINGLELINE', "ips")
        self.admin.assert_icommand("iqstat", 'STDOUT_SINGLELINE', "No delayed rules")
        self.admin.assert_icommand("ils -l " + irodshome + "/icmdtest1/foo1", 'STDOUT_SINGLELINE', ["foo1", myssize])
        self.admin.assert_icommand("iadmin ls " + irodshome + "/icmdtest1", 'STDOUT_SINGLELINE', "foo1")
                   'STDOUT_SINGLELINE', self.user0.username + "#" + irodszone + ":read")
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest1/foo1", 'STDOUT_SINGLELINE', "testmeta1")
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest1/foo1", 'STDOUT_SINGLELINE', "180")
        self.admin.assert_icommand("imeta ls -d " + irodshome + "/icmdtest1/foo1", 'STDOUT_SINGLELINE', "cm")
        self.admin.assert_icommand("ichksum -K " + irodshome + "/icmdtest1/foo2", 'STDOUT_SINGLELINE', "foo2")
                   lrsfile + " -N 2 " + myldir + " " + irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "New restartFile")
        self.admin.assert_icommand("ichksum -rK " + irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "Total checksum performed")
                   irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "icmdtest/testy")
                   irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "This is a DRYRUN")
                   irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "a copy trimmed")
                   irodshome + "/icmdtest/testz", 'STDOUT_SINGLELINE', "Processing lfile1")
                   self.testresc + " " + irodshome + "/icmdtest/testz", 'STDOUT_SINGLELINE', "icmdtest/testz")
                   " --rlock -N 2 " + irodshome + "/icmdtest/testz " + dir_w + "/testz", 'STDOUT_SINGLELINE', "testz")
    @unittest.skipIf(configuration.USE_SSL, 'RBUDP does not support encryption')
                   lrsfile + " " + myldir + " " + irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "icmdtest/testy")
                   irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "icmdtest/testy")
                   irodshome + "/icmdtest/testy", 'STDOUT_SINGLELINE', "a copy trimmed")
                   irodshome + "/icmdtest/testz", 'STDOUT_SINGLELINE', "Processing sfile1")
                   " " + irodshome + "/icmdtest/testz " + dir_w + "/testz", 'STDOUT_SINGLELINE', "Processing sfile2")